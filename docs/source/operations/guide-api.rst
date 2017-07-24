Armada RESTful API
===================

Armada Endpoints
-----------------

.. http:post:: /armada/apply

    :string file   armada manifest
    :>json boolean debug Enable debug logging
    :>json boolean disable_update_pre
    :>json boolean disable_update_post
    :>json boolean enable_chart_cleanup
    :>json boolean skip_pre_flight
    :>json boolean dry_run
    :>json boolean wait
    :>json float timeout

    Request:

    .. sourcecode:: js

        {
        	"file": "<manifest-payload>",
        	"options": {
        		"debug": true,
        		"disable_update_pre": false,
        		"disable_update_post": false,
        		"enable_chart_cleanup": false,
        		"skip_pre_flight": false,
        		"dry_run": false,
        		"wait": false,
        		"timeout": false
        	}
        }

    Results:

    .. sourcecode:: js

        {
            "success": True
        }

Tiller Endpoints
-----------------

.. http:get:: /tiller/releases

    Retrieves tiller releases.

    Results:

    .. sourcecode:: js

    {
        "releases": {
            "<namespace-name>": [
                "armada-memcached",
                "armada-etcd",
                "armada-rabbitmq",
            ]
        }
    }

.. http:get:: /tiller/status

    Retrieves the status of the Tiller server.

    Results:

    .. sourcecode:: js

    {
        "message": Tiller Server is Active
    }
