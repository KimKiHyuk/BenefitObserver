#!/bin/bash
 
for (( ; ; ))
do
   scrapy crawl HallymSoftwareSpider
   echo "Pres CTRL+C to stop..."
   sleep 1
done
