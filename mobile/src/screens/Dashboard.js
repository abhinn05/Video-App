import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, Image, TouchableOpacity } from 'react-native';
import client from '../api/client';

export default function Dashboard({ navigation }) {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    client.get('/dashboard').then(res => setVideos(res.data)); // [cite: 31]
  }, []);

  return (
    <FlatList
      data={videos}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => (
        <TouchableOpacity onPress={() => navigation.navigate('Player', { id: item.id })}>
          <Image source={{ uri: item.thumbnail_url }} style={{ width: '100%', height: 200 }} />
          <Text style={{ fontWeight: 'bold' }}>{item.title}</Text> 
          <Text>{item.description}</Text> 
        </TouchableOpacity>
      )}
    />
  );
}