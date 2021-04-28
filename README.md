# Colab-Socket

```
gcloud beta compute --project=magmask instances create magmask-socket-server --zone=us-central1-a --machine-type=f1-micro --subnet=default --network-tier=STANDARD --can-ip-forward --maintenance-policy=MIGRATE --service-account=33463977803-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server,https-server --image=debian-10-buster-v20210420 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-balanced --boot-disk-device-name=socket-server --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any
```
Modify GCP firewall rule `default-allow-internal` and add `0.0.0.0/0` under source filter
