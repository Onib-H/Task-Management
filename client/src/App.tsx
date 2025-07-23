import './App.css'
import { Route, Routes } from 'react-router-dom'
import Homepage from './pages/Homepage'
import UserDashboard from './pages/user/UserDashboard'

function App() {
  return (
    <Routes>
      <Route path='/' element={<Homepage />} />
      <Route path='/user' element={<UserDashboard />} />
    </Routes>
  )
}

export default App
