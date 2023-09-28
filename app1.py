


# assume this is a dummy app, there are some http requests needed to be sent to the cloud.
# before each http is sent, we invoke one dns service that provided by c-ares library,
# like using one udp socket to trigger the dns process and got the ip and flag back

# in terms of issuing http requests, some http requests should be issued sequentially,
# but some of them need to be sent in parallel based on the app logic DAG



