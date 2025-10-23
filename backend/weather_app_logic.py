# Import the module.
import python_weather

import asyncio
import os


async def fetch_weather(city: str, unit: str = python_weather.IMPERIAL) -> dict:
    """Fetch weather for `city` and return a serializable dict.

    This is an async function you can `await` from other async code (for example,
    directly from a FastAPI route). A small sync wrapper `fetch_weather_sync` is
    provided for convenience in synchronous contexts.
    """

    async with python_weather.Client(unit=unit) as client:
        weather = await client.get(city)

        result: dict = {
            "city": city,
            "temperature": weather.temperature,
            "days": [],
        }

        for daily in weather:
            day = {
                "repr": repr(daily),
                # try to pull common attributes if present
                "date": getattr(daily, "date", None),
                "temperature": getattr(daily, "temperature", None),
                "hourly": [],
            }

            for hourly in daily:
                day["hourly"].append({
                    "repr": repr(hourly),
                    # add any fields you need here, e.g. "temp": getattr(hourly, "temperature", None)
                })

            result["days"].append(day)

        return result

def fetch_weather_sync(city: str, unit: str = python_weather.IMPERIAL) -> dict:
    """Synchronous wrapper for `fetch_weather` for use in sync code or quick tests."""
    return asyncio.run(fetch_weather(city, unit=unit))


if __name__ == '__main__':
    # Quick manual test when running the file directly.
    # If you hit Windows-specific asyncio issues uncomment the guarded block below.
    # See https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for background.
    # if os.name == 'nt':
    #     wssp = getattr(asyncio, "WindowsSelectorEventLoopPolicy", None)
    #     if wssp is not None:
    #         asyncio.set_event_loop_policy(wssp())

    data = fetch_weather_sync("New York")
    print(data)