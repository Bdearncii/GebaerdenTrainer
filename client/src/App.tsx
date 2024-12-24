import { Route, Routes, Router} from 'react-router-dom';
import Home from "./pages/Home";
import Login from "./pages/Login"


function App() {
  return (
    <Routes>
      <Route index element={<Home />} />
      <Route path="/signin" element={<Login />} />
    </Routes>
  );
};

export default App
