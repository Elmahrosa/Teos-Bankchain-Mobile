import React, {useEffect, useState} from 'react';
import { View, Text, Button, FlatList } from 'react-native';
import axios from 'axios';

export default function DashboardScreen({ route, navigation }) {
  const { token } = route.params || {};
  const [wallets, setWallets] = useState([]);

  useEffect(() => {
    async function load() {
      try {
        const res = await axios.get('http://10.0.2.2:8000/wallets');
        setWallets(res.data);
      } catch (e) {
        console.log(e.message);
      }
    }
    load();
  }, []);

  return (
    <View style={{flex:1,padding:20}}>
      <Text style={{fontSize:20,fontWeight:'bold'}}>My Wallets</Text>
      <FlatList
        data={wallets}
        keyExtractor={item => String(item.id)}
        renderItem={({item}) => (
          <View style={{padding:12,borderBottomWidth:1,borderColor:'#eee'}}>
            <Text style={{fontWeight:'bold'}}>{item.name} — {item.currency}</Text>
            <Text>Balance: {item.balance}</Text>
            <Button title="Open" onPress={() => navigation.navigate('Wallet', { walletId: item.id })} />
          </View>
        )}
      />
    </View>
  );
}