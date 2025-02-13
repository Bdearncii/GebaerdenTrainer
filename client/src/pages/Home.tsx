import { useNavigate } from 'react-router-dom';
import Button from '@mui/material/Button';
import { Stack } from '@mui/material';

function Home() {
    const navigate = useNavigate();

    const handleLoginClick = () => {
        navigate("/login");
    };

    const handleSignUpClick = () => {
        navigate("/sign-up");
    };

    return (
        <>
            <h1>Welcome to GebärdenTrainer!</h1>
            <Stack spacing={2} direction="row">
                <Button variant="contained" onClick={handleLoginClick}>Login</Button>
                <Button variant="contained" onClick={handleSignUpClick}>Sign Up</Button>
            </Stack>
        </>
    );
}

export default Home;