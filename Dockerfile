FROM ubuntu:latest
MAINTAINER Alison Comrie <aecomrie@email.arizona.edu>
RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install libhdf5-serial-dev
RUN apt-get -y install netcdf-bin
RUN apt-get -y install libnetcdf-dev
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install -U pip
RUN pip install h5py
RUN HDF5_DIR=/usr/local/hdf5
RUN pip install netCDF4
RUN pip install plotly
ADD hw7.py hw7.py
VOLUME /data
