from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

tz_sh = ZoneInfo("Asia/Shanghai")
tz_utc = ZoneInfo("UTC")
tz_ny = ZoneInfo("America/New_York")

sh_t1 = datetime.now(tz=tz_sh)
ny_t1 = sh_t1.astimezone(tz=tz_ny)
utc_t1 = sh_t1.astimezone(tz=tz_utc)

print(f"上海时间: {sh_t1.strftime('%Y-%m-%d %H:%M:%S %z')}")
print(f"纽约时间: {ny_t1}")
print(f"UTC时间: {utc_t1}")

td = timedelta(days=1, hours=6)
sh_t2 = sh_t1 + td
print(f"上海时间: {sh_t2.strftime('%Y-%m-%d %H:%M:%S %z')}")