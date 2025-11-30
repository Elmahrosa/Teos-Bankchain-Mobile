import React, {useState} from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
import axios from 'axios';
import { registerForPushNotificationsAsync } from '../../services/push';

export default function LoginScreen({ navigation }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const onLogin = async () => {
    try {
      const res = await axios.post('http://10.0.2.2:8000/auth/login', { email, password });
      const token = res.data.access_token;
      try {
        const pushToken = await registerForPushNotificationsAsync();
        if(pushToken){ await axios.post('http://10.0.2.2:8000/push/register', { token: pushToken, user_id: null }); }
      } catch(e){ console.log('push register', e.message) }
      navigation.replace('Dashboard', { token });
    } catch (e) {
      Alert.alert('Login failed', e.response?.data?.detail || e.message);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>TEOS BankChain — Login</Text>
      <TextInput placeholder="Email" style={styles.input} onChangeText={setEmail} autoCapitalize="none" />
      <TextInput placeholder="Password" style={styles.input} secureTextEntry onChangeText={setPassword} />
      <Button title="Login" onPress={onLogin} />
    </View>
  );
}

const styles = StyleSheet.create({
  container:{flex:1,justifyContent:'center',padding:20},
  title:{fontSize:22,fontWeight:'bold',marginBottom:20},
  input:{height:50,borderColor:'#ccc',borderWidth:1,borderRadius:6,padding:10,marginBottom:12}
});