import { createNativeStackNavigator } from "@react-navigation/native-stack";

import Register from "../screens/Register";

const Stack = createNativeStackNavigator();

export function AppRoutes() {
    return (
        <Stack.Navigator>
            <Stack.Screen
                name="Register"
                component={Register}
            />
        </Stack.Navigator>
    );
}