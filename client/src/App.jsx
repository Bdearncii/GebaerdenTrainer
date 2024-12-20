import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0);
  const [username, setUsername] = useState('');  // Zustand für den Benutzernamen
  const [password, setPassword] = useState('');  // Zustand für das Passwort
  const [message, setMessage] = useState('');  // Zustand für die Antwort vom Server
  const [error, setError] = useState('');  // Zustand für Fehlermeldungen

  // Funktion zum Handhaben des Login-Versuchs
  const handleLogin = async (e) => {
    e.preventDefault();

    // Sende eine POST-Anfrage an das Flask-Backend
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: username,
          password: password,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        // Erfolgreiche Anmeldung, zeige Nachricht an
        setMessage(data.message);
        setError('');  // Fehlermeldung zurücksetzen
      } else {
        // Fehler beim Login, zeige Fehlermeldung an
        setError(data.error);
        setMessage('');  // Erfolgsnachricht zurücksetzen
      }
    } catch (err) {
      setError('An error occurred: ' + err.message);
      setMessage('');  // Erfolgsnachricht zurücksetzen
    }
  };

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>

      <h1>Login to your account</h1>

      {/* Login-Formular */}
      <form onSubmit={handleLogin}>
        <div>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>

      {/* Anzeige der Serverantwort */}
      {message && <div className="message success">{message}</div>}
      {error && <div className="message error">{error}</div>}

      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;
