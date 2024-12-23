import { useNavigate } from 'react-router-dom';
import Button from '@mui/material/Button';

function Home() {
    const navigate = useNavigate();

    const handleLoginClick = () => {
        navigate("/login");
    };

    return (
        <>
            <h1>Welcome to GebärdenTrainer!</h1>
            <Button variant="contained" onClick={handleLoginClick}>Login</Button>
        </>
    );
}

export default Home;