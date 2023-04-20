### Developing a Dockerfile

A Dockerfile is a text file that contains a list of instructions, each of which is a layer of images.
In general, a Dockerfile is divided into 4 parts:

- Base image
- Maintainer information
- Image operation commands
- commands to be executed when the container is started

When creating a mirror, the following points need to be considered:

- The naming initials must be in upper case;
- the referenced files must be in the current directory and its following subdirectories
- if there are files that do not need to be packaged, these can be recorded in a hidden file (.dockeringore) in the current directory;

Its important command fields are:

- FROM: specifies the base image
- COPY: copies files to the container
- ADD: add local files or URLs to the container
- ENV: Specify environment variables
- RUN: Specify the command to execute when building
- CMD: Specify the command to execute at startup
- ENTRYPOINT: Specify the command to be executed at startup
- EXPOSE: specifies the exposed port
- ARG: Specify the parameter that can be passed in during `docker build`.
- VOLUME: specify the container mount point
- LABEL: specify the container label

> PS: Here is only a brief introduction to Dockerfile, more operations need to be learned in private.

Now let's write the Dockerfile for `go-hello-world`.

Since our project is a simple WEB developed with Go, we can use `go build` to package the application directly, so our Dockerfile can be as follows:

```dockerfile
FROM golang
ENV GOPROXY https://goproxy.cn
ADD . /app
WORKDIR /app
RUN go mod tidy
RUN GOOS=linux GOARCH=386 go build -v -o /app/go-hello-word
CMD [". /go-hello-world"]
```

If pulling the dependency package times out, you can change the Dockerfile to the following:

```dockerfile
FROM golang
ADD . /app
WORKDIR /app
RUN go env -w GOPROXY=https://goproxy.cn,direct && go mod tidy
RUN GOOS=linux GOARCH=386 go build -v -o /app/go-hello-word
CMD [". /go-hello-world"]
```

The Go developed application is finally produced as a binary executable, if we follow the above Dockerfile for mirroring, we will package unnecessary source code as well, which causes a serious waste of resources, for this reason, we can use **multi-stage build**, Dockerfile transformation as follows:

```dockerfile
FROM golang AS build-env
ENV GOPROXY https://goproxy.cn
ADD . /go/src/app
WORKDIR /go/src/app
RUN go mod tidy
RUN GOOS=linux GOARCH=386 go build -v -o /go/src/app/go-hello-world

FROM alpine
COPY --from=build-env /go/src/app/go-hello-world /usr/local/bin/go-hello-world
EXPOSE 8080
CMD [ "go-hello-world" ]
```

This way, the only image we end up making is the executable binary.

Now, we can create a `Dockerfile` file in the source root directory and write the above.

The image can then be built using the following command:

```bash
docker build -t 10.111.127.141:30002/dev/go-hello-world:v0.0.1 .
```

The output is as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/0d69857585cf1da833ac09b6d3b3d7e1-0/wm)

Push the image to the Harbor repository with the following command:

```bash
docker push 10.111.127.141:30002/dev/go-hello-world:v0.0.1
```
