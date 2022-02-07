for /f %%i in ('docker ps -q -f "name=gem5"' ) do set gem5_running=%%i
if [%gem5_running%]==[] docker run -d --volume gem5_volume:/gem5 --rm -it --name="gem5" gem5

REM copying additional files used as parameters not yet supported
docker cp ../../example_md5/data/file_1MB.txt gem5:/usr/local/src/gem5/file_1MB.txt
docker cp ../../example_md5/data/file_2MB.txt gem5:/usr/local/src/gem5/file_2MB.txt
docker cp ../../example_md5/data/file_3MB.txt gem5:/usr/local/src/gem5/file_3MB.txt