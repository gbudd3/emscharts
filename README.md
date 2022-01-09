# emscharts

sqlite> select dispatch_id, date_dispatched,date_enroute,(strftime('%s',date_enroute) - strftime('%s',datetime(date_dispatched))) /60 from charts limit 5;
E180040005|2018-04-01 01:09:00|2018-04-01 01:28:00|19
E180050006|2018-05-01 03:45:00|2018-05-01 04:04:00|19
E180050009|2018-05-01 05:36:00|2018-05-01 05:36:00|0
E180070003|2018-07-01 00:28:00|2018-07-01 00:39:00|11
E180070022|2018-07-01 11:00:00|2018-07-01 11:06:00|6
