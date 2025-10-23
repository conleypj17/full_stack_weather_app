import React, { useState } from 'react';

export default function WeatherApp() {
    const [weather, setWeather] = useState(null);
    const [city, setCity] = useState('New York');

    const getWeather = async () => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/weather/${city}`);
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            const data = await response.json();
            setWeather(data);
        } catch (error) {
            console.error("Error fetching weather:", error);
        }
    };

    return (
        <div>
            <h1>Weather App</h1>
            <input
                type="text"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                placeholder="Enter city"
            />
            <button onClick={getWeather}>Get Weather</button>

            {weather && (
                <div>
                    <h2>City: {weather.city}</h2>
                    <p>Temperature: {weather.temperature}</p>
                </div>
            )}
        </div>
    );

}