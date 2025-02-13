import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom';

import RootLayout from './layouts/Root-Layout';
import AuthLayout from './layouts/Auth-Layout';

import Home from './pages/Home';
import SignUp from './pages/SignUp';
import Login from './pages/Login';

function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        <Route path='/' element={<RootLayout />}>
          <Route index element={<Home />} />
        </Route>

        <Route element={<AuthLayout />}>
          <Route path='/sign-up' element={<SignUp />} />
          <Route path='/login' element={<Login />} />
        </Route>
      </>
    )
  );

  return <RouterProvider router={router} />;
}

export default App;