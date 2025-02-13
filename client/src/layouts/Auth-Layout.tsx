import { useEffect } from 'react';
import { Outlet } from 'react-router-dom';

const AuthLayout = () => {
  useEffect(() => {
    // Change body styles for authentication pages
    document.body.style.background = "url('/assets/authentication_background.jpg') no-repeat center center fixed";
    document.body.style.backgroundSize = "cover";
    document.body.style.height = "100vh";
    document.body.style.margin = "0";

    return () => {
      // Reset styles when leaving authentication pages
      document.body.style.background = "";
      document.body.style.height = "";
      document.body.style.margin = "";
    };
  }, []);

  return (
    <Outlet />
  );
};

export default AuthLayout;