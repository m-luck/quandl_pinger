# API Key from Quandl is $1
# Data in format YYYYMMDD is $2
# Download the file, unzip it, and run spx 
wget -O OSMV-$2.zip "https://www.quandl.com/api/v3/databases/OSMV/download?download_type=$2&api_key=$1" && 
unzip OSMV-$2.zip && 
python OSMV_to_spx-spot_px.py OSMV-$2.csv &&
# Comment the two lines below if you want to retain the original zip and csv downloaded. 
rm OSMV-$2.zip &&
rm OSMV-$2.csv