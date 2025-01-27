const API = import.meta.env.VITE_API_ENDPOINT;
import { AppProvider } from '@toolpad/core/AppProvider';
import { SignInPage, type AuthProvider } from '@toolpad/core/SignInPage';
import { useTheme } from '@mui/material/styles';
import imageLogo from '../../assets/logo_horizontal.png';
import axios from 'axios';

const handleLogin = async (username: string, password: string) => {
  try {
    const response = await axios.post(API+'/login', {
      username,
      password,
    });

    if (response.status === 202) {
      console.log(response.data.message);
      alert('Registration successful!');
    }
  } catch (error: any) {
    if (error.response) {
      console.error(error.response.data.error);
      alert(`Error: ${error.response.data.error}`);
    } else {
      console.error('Login failed');
      alert('Login failed. Please try again.');
    }
  }
};

const providers = [
  { id: 'google', name: 'Google' },
  { id: 'credentials', name: 'Credentials' },
];

const BRANDING = {
  logo: (
    <img
      src={imageLogo}
      alt="GebärdenTrainer Logo"
      style={{ height: 70 }}
    />
  ),
};

const signIn: (provider: AuthProvider, formData: FormData) => void = async (
  provider,
  formData,
) => {
  if (provider.id === 'credentials' && formData) {
    const username = formData.get('email') as string;
    const password = formData.get('password') as string;

    await handleLogin(username, password);
  } else {
    console.log(`Sign in with ${provider.id}`);
  }
};

export default function SignIn() {
  const theme = useTheme();
  return (
    <AppProvider branding={BRANDING} theme={theme}>
      <SignInPage
        signIn={signIn}
        providers={providers}
        slotProps={{
          emailField: { autoFocus: false },
          submitButton: {
            sx: {
              backgroundColor: 'green',
              '&:hover': {
                backgroundColor: 'darkgreen',
              },
              marginTop: 2,
            },
          },
        }}
      />
    </AppProvider>
  );
}
