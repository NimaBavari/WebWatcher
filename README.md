# WebWatcher

_by Tural Mahmudov <nima.bavari@gmail.com>_

**Time taken: 2 hours**

Event-driven website monitoring service.

## Scripts

### Dev Scripts

Run

```sh
chmod +x ./lint.sh
./lint.sh
```

to lint and format the code in the directory of this project.

### Usage

Run `docker-compose up producer` to start up the producer at any machine/server/cluster.

Run `docker-compose up consumer` to start up the consumer at any machine/server/cluster.

Run `docker-compose up test` to spin up the tests.
