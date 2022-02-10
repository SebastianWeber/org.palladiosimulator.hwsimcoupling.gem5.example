for /f %%i in ('docker ps -q -f "name=gem5"' ) do set gem5_running=%%i
if [%gem5_running%]==[] docker run -d --volume gem5_volume:/gem5 --rm -it --name="gem5" gem5