import React, {useEffect, useState} from 'react';
import { View, Text, Button, TextInput, Alert } from 'react-native';
import axios from 'axios';

export default function WalletScreen({ route }) {
  const { walletId } = route.params;
  const [wallet, setWallet] = useState(null);
  const [amount, setAmount] = useState('');

  useEffect(() => {
    async function load() {
      try {
        const res = await axios.get(`http://10.0.2.2:8000/wallets/${walletId}`);
        setWallet(res.data);
      } catch (e) {
        console.log(e.message);
      }
    }
    load();
  }, []);

  const sendTx = async () => {
    try {
      const res = await axios.post('http://10.0.2.2:8000/transactions', { amount: parseFloat(amount), to_address: 'receiver' }, { params: { wallet_id: walletId }});
      Alert.alert('Sent', JSON.stringify(res.data));
    } catch (e) {
      Alert.alert('Error', e.response?.data?.detail || e.message);
    }
  };

  if (!wallet) return <View><Text>Loading...</Text></View>;

  return (
    <View style={{flex:1,padding:20}}>
      <Text style={{fontSize:20,fontWeight:'bold'}}>{wallet.name}</Text>
      <Text>Balance: {wallet.balance}</Text>
      <TextInput placeholder="Amount" value={amount} onChangeText={setAmount} keyboardType="numeric" style={{borderWidth:1,padding:8,marginVertical:12}} />
      <Button title="Send" onPress={sendTx} />
    </View>
  );
}