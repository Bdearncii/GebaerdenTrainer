import { AppProvider } from '@toolpad/core/AppProvider';
import { SignInPage, type AuthProvider } from '@toolpad/core/SignInPage';
import { useTheme } from '@mui/material/styles';
import imageLogo from '../../assets/logo_horizontal.png';

const providers = [
  { id: 'google', name: 'Google' },
  { id: 'credentials', name: 'Credentials' }];
const BRANDING = {
  logo: (
    <img
      src= {imageLogo}
      alt="GebärdenTrainer Logo"
      style={{ height: 70 }}
    />
  )
};

const signIn: (provider: AuthProvider) => void = async (provider) => {
  const promise = new Promise<void>((resolve) => {
    setTimeout(() => {
      console.log(`Sign in with ${provider.id}`);
      resolve();
    }, 500);
  });
  return promise;
};

export default function Login() {
  const theme = useTheme();
  return (
    <AppProvider branding={BRANDING} theme={theme}>
      <SignInPage

        signIn={signIn}
        providers={providers}
        slotProps={{ emailField: { autoFocus: false },
        submitButton: {
          sx: {
            backgroundColor: 'green',
            '&:hover': {
              backgroundColor: 'darkgreen'
            },
            marginTop: 2,
          }
        }
      }}
      /> 
      
      </AppProvider>
  );
}