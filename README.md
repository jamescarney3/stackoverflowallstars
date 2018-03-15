# StackOverflowAllStars

### MVP Reqs
- Store screenshots
- Tweet screenshots at fixed intervals from @stackoverflowas

### Provisional MVP Structure
#### Storage
 - S3 bucket with 2 subdirs (one queue, one archive)

#### Automation

- AWS runs a python script - Run function on schedule (fixed rate or cron):

```
if any screenshot imgs exist in queue subdir:
	pick oldest img from queue subdir
	tweet img from @stackoverflowas
	move img to archive subdir
else
	pick random img from archive subdir
	tweet img from @stackoverflowas
```
#### Integration
- Python <=> Twitter: [Twython](https://twython.readthedocs.io/en/latest/)
- Python <=> S3: [Boto](https://github.com/boto/boto)


### Future Roadmap
- web admin interface to upload screenshot imgs to AWS