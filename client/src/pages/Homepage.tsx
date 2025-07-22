import { getMessage } from "../services/Chat"
import { useQuery } from "@tanstack/react-query"
import { Link } from "react-router-dom";

const Homepage = () => {
    const { data, isLoading, error } = useQuery({
        queryKey: ['message'],
        queryFn: getMessage,
    });

    if (isLoading) return <div className="text-2xl">Loading...</div>
    if (error) return <div className="text-2xl">Error: {error.message}</div>
    
    return (
        <div className="text-2xl">
            <h1>{data.message}</h1>
            <Link to="/guest" className="underline">Go to Guest Page</Link>
        </div>
    )
}

export default Homepage