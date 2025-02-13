import { useState } from "react";
import {
    Box,
    Button,
    TextField,
    Typography,
    Divider,
    Grid,
    Link,
} from "@mui/material";
import { styled, ThemeProvider, createTheme } from "@mui/material/styles";
import { Google as GoogleIcon, Facebook as FacebookIcon } from "@mui/icons-material";
import { useNavigate } from "react-router-dom";

const theme = createTheme({
    palette: {
        primary: {
            main: "#00bfa5",
        },
        secondary: {
            main: "#0288d1",
        },
        background: {
            default: "linear-gradient(135deg, #004d40, #003366)",
        }
    },
    typography: {
        fontFamily: "Bahnschrift",
    },
});

const GradientBackground = styled(Box)({
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    minHeight: "100vh",
    width: "100vw",
    margin: 0,
    padding: 0
});

const FormContainer = styled(Box)({
    width: "100%",
    maxWidth: 400,
    backgroundColor: "white",
    padding: 24,
    borderRadius: 12,
    boxShadow: "0px 4px 20px rgba(0, 0, 0, 0.2)",
});

const LoginPage: React.FC = () => {
    const [formData, setFormData] = useState({
        email: "",
        password: "",
    });
    const [errors, setErrors] = useState<{ [key: string]: string }>({});

    const handleChange = (
        e: React.ChangeEvent<HTMLInputElement>
    ): void => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const validate = (): boolean => {
        let isValid = true;
        const newErrors: { [key: string]: string } = {};

        if (!formData.email.includes("@")) {
            isValid = false;
            newErrors.email = "Please enter a valid email.";
        }

        if (formData.password.length < 6) {
            isValid = false;
            newErrors.password = "Password must be at least 6 characters.";
        }

        setErrors(newErrors);
        return isValid;
    };

    const handleSubmit = (): void => {
        if (validate()) {
            console.log("Form submitted", formData);
            // Handle successful login logic
        }
    };

    
    const navigate = useNavigate();

    const redirectToSignUp = () => {
      navigate("/sign-up");
    };

    return (
        <ThemeProvider theme={theme}>
            <GradientBackground>
                <FormContainer>
                    <Typography
                        variant="h5"
                        component="h1"
                        color="primary"
                        align="center"
                        gutterBottom
                    >
                        Login
                    </Typography>

                    <TextField
                        label="Email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        error={!!errors.email}
                        helperText={errors.email}
                        fullWidth
                        margin="normal"
                        variant="outlined"
                    />

                    <TextField
                        label="Password"
                        name="password"
                        type="password"
                        value={formData.password}
                        onChange={handleChange}
                        error={!!errors.password}
                        helperText={errors.password}
                        fullWidth
                        margin="normal"
                        variant="outlined"
                    />

                    <Box textAlign="right" sx={{ mt: 1, mb: 2 }}>
                        <Link href="#" variant="body2" color="primary">
                            Forgot password?
                        </Link>
                    </Box>

                    <Button
                        variant="contained"
                        color="primary"
                        fullWidth
                        sx={{ mt: 2, mb: 2 }}
                        onClick={handleSubmit}
                    >
                        Login
                    </Button>

                    <Divider sx={{ my: 2, fontFamily: "Bahnschrift" }}>or</Divider>

                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <Button
                                variant="outlined"
                                fullWidth
                                startIcon={<GoogleIcon />}
                            >
                                Login with Google
                            </Button>
                        </Grid>
                        <Grid item xs={12}>
                            <Button
                                variant="outlined"
                                fullWidth
                                startIcon={<FacebookIcon />}
                                color="secondary"
                            >
                                Login with Facebook
                            </Button>
                        </Grid>
                    </Grid>

                    <Typography
                        variant="body2"
                        align="center"
                        sx={{ mt: 3 }}
                    >
                        Don't have an account? <Button color="primary" size="small" onClick={redirectToSignUp}>Sign Up</Button>
                    </Typography>
                </FormContainer>
            </GradientBackground>
        </ThemeProvider>
    );
};

export default LoginPage;