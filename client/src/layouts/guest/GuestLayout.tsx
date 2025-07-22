import { Outlet } from "react-router-dom"
import GuestSidebar from "./GuestSidebar"
import Footer from "../Footer"

const GuestLayout = () => {
    return (
        <div>
            <GuestSidebar />
            <Outlet />
            <Footer />
        </div>
    )
}

export default GuestLayout