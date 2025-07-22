import './App.css'
import { Route, Routes } from 'react-router-dom'
import Homepage from './pages/Homepage'
import GuestLayout from './layouts/guest/GuestLayout'
import GuestHomepage from './pages/guest/GuestHomepage'

function App() {
  return (
    <Routes>
      <Route path='/' element={<Homepage />} />
      <Route path='/guest' element={<GuestLayout />}>
        <Route index element={<GuestHomepage />} />
      </Route>
    </Routes>
  )
}

export default App
