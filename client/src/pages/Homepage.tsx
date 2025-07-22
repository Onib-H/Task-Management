import { getMessage } from "../services/Chat"
import { useQuery } from "@tanstack/react-query"

const Homepage = () => {
    const { data, isLoading, error } = useQuery({
        queryKey: ['message'],
        queryFn: getMessage,
    });

    if (isLoading) return <div className="text-2xl">Loading...</div>
    if (error) return <div className="text-2xl">Error: {error.message}</div>
    
    return (
        <div className="text-2xl underline">{data.message}</div>
    )
}

export default Homepage