import { useNavigate } from 'react-router-dom';
import Button from '@mui/material/Button';

function Home() {
    const navigate = useNavigate();

    const handleLoginClick = () => {
        navigate("/signin");
    };

    return (
        <>
            <h1>Welcome to GebärdenTrainer!</h1>
            <Button variant="contained" onClick={handleLoginClick}>Sign In</Button>
        </>
    );
}

export default Home;