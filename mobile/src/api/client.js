import axios from 'axios';
import * as SecureStore from 'expo-secure-store'; // [cite: 28]

const client = axios.create({ baseURL: 'http://YOUR_LOCAL_IP:5000' });

client.interceptors.request.use(async (config) => {
  const token = await SecureStore.getItemAsync('userToken');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default client;