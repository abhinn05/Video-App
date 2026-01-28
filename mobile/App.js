import React, { useState, useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import * as SecureStore from 'expo-secure-store';

import LoginScreen from './src/screens/LoginScreen';
import Dashboard from './src/screens/Dashboard';
import PlayerScreen from './src/screens/PlayerScreen';

const Stack = createStackNavigator();

export default function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [userToken, setUserToken] = useState(null);

  useEffect(() => {
    // On success: Store JWT securely [cite: 28]
    const checkToken = async () => {
      const token = await SecureStore.getItemAsync('userToken');
      setUserToken(token);
      setIsLoading(false);
    };
    checkToken();
  }, []);

  return (
    <NavigationContainer>
      <Stack.Navigator>
        {userToken == null ? (
          // Auth Screens [cite: 19]
          <Stack.Screen name="Login" component={LoginScreen} />
        ) : (
          // Authenticated Screens
          <>
            <Stack.Screen name="Dashboard" component={Dashboard} />
            <Stack.Screen name="Player" component={PlayerScreen} />
          </>
        )}
      </Stack.Navigator>
    </NavigationContainer>
  );
}