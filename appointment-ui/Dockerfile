
FROM node:16.10.0-alpine3.13 as build-stage
 

# make the 'app' folder the current working directory
WORKDIR /app
 
# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./
 
# install project dependencies
RUN npm install
 
# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .
 
# build app for production with minification
RUN npm run build

# Use the lightweight Nginx image from the previous stage for the nginx container
FROM nginx:stable-alpine as production-stage

# Copy the build application from the previous stage to the Nginx container
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy the nginx configuration file
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# Expose the port 80
EXPOSE 80

# DEBUG = TRUE

# Start Nginx to serve the application
CMD ["nginx", "-g", "daemon off;"]
































# #FROM node:16.10.0-alpine3.13 as build-stage
# FROM node:lts-alpine as build-stage
 
# # install simple http server for serving static content
# # RUN npm install -g http-server
 
# # make the 'app' folder the current working directory
# WORKDIR /app
 
# # copy both 'package.json' and 'package-lock.json' (if available)
# COPY package*.json ./
 
# # install project dependencies
# RUN npm install
 
# # copy project files and folders to the current working directory (i.e. 'app' folder)
# COPY . .
 
# # build app for production with minification
# RUN npm run build

# # Use the lightweight Nginx image from the previous stage for the nginx container
# FROM nginx:stable-alpine as production-stage

# # Copy the build application from the previous stage to the Nginx container
# COPY --from=build-stage /app/dist /usr/share/nginx/html

# # Copy the nginx configuration file
# COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# # Expose the port 80
# EXPOSE 8080

# # Start Nginx to serve the application
# CMD ["nginx", "-g", "daemon off;"]
