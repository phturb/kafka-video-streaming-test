Run each file as their own worker

```
faust -A video_producer worker -l info --web-port 6068
faust -A consumer worker -l info --web-port 6069
faust -A image_update worker -l info --web-port 6070
faust -A consumer_raw worker -l info --web-port 6071

```
