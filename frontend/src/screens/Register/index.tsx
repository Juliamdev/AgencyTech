import { View, Text } from "react-native";
import { Input } from "../../components/Input";
import { useState } from "react";
import { Button } from "../../components/Button";
import { styles } from "./styles";
import { api } from "../../services/api";

export default function Register() {

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    const validateForm = () => {
        if (!username || !email || !password || !confirmPassword) {
            alert("Please fill in all fields.");
            return false;
        }
        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return false;
        }
        return true;
    }

    const _handleRegister = () => {
        if (!validateForm()) {
            return;
        }

        const res = api.post("/users", {
            username,
            email,
            password
        }).then((response) => {
            alert("User registered successfully!");
        }).catch((error) => {
            console.error(error);
        });
    };

    return (
        <View style={styles.container}>
            <Input 
                placeholder="Enter your username"
                value={username}
                onChangeText={setUsername}
            />
            <Input 
                placeholder="Enter your email"
                value={email}
                onChangeText={setEmail}
            />
            <Input 
                placeholder="Enter your password"
                secureTextEntry
                value={password}
                onChangeText={setPassword}
            />
            <Input
                placeholder="Confirm your password"
                secureTextEntry
                value={confirmPassword}
                onChangeText={setConfirmPassword}
            />
            <Button title="Register" onPress={_handleRegister} />
        </View>
    );
}