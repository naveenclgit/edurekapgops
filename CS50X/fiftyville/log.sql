-- Keep a log of any SQL queries you execute as you solve the mystery.


-- theft took place on July 28, 2021 and that it took place on Humphrey Street.
--it helpful to start with the crime_scene_reports table
SELECT id, description, street
  FROM crime_scene_reports
  WHERE year = 2021
  AND month = 7
  AND day = 28 ;

-- adding street to filter
SELECT id, description, street
  FROM crime_scene_reports
  WHERE year = 2021
   AND month = 7
   AND day = 28
   AND street = 'Humphrey Street';

-- 295 Interviews were conducted today with three witnesses who were present
-- at the time – each of their interview transcripts mentions the bakery

SELECT name, transcript
FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28
AND transcript LIKE '%bakery%'
ORDER BY name;

-- Eugene - ATM at Leggett Street
SELECT account_number, amount
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

/*
Get Person id based on account number
SELECT person_id
FROM bank_accounts
WHERE account_number IN (SELECT account_number
                            FROM atm_transactions
                            WHERE year = 2021
                            AND month = 7
                            AND day = 28
                            AND atm_location = 'Leggett Street'
                            AND transaction_type = 'withdraw');
*/
-- get suspects list
SELECT  *
FROM people
WHERE id IN (SELECT person_id
FROM bank_accounts
WHERE account_number IN (SELECT account_number
                            FROM atm_transactions
                            WHERE year = 2021
                            AND month = 7
                            AND day = 28
                            AND atm_location = 'Leggett Street'
                            AND transaction_type = 'withdraw'));


-- Raymond - Phone call - earliest flight out of Fiftyville - other guy purchase ticket
SELECT flights.id, full_name, city, flights.hour, flights.minute
FROM airports
JOIN flights
ON airports.id = flights.destination_airport_id
WHERE flights.origin_airport_id = (SELECT id
                                    FROM airports
                                    WHERE city = 'Fiftyville')
AND flights.year = 2021
AND flights.month = 7
AND flights.day = 29
ORDER BY flights.hour, flights.minute;

-- Get passsengers on flights from Fiftyville
SELECT passengers.flight_id, name, passengers.passport_number, passengers.seat
FROM people
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON passengers.flight_id = flights.id
WHERE flights.year = 2021
AND flights.month = 7
AND flights.day = 29
AND flights.hour = 8
AND flights.minute = 20
AND flights.id IN (SELECT flights.id FROM airports
                    JOIN flights
                    ON airports.id = flights.destination_airport_id
                    WHERE flights.origin_airport_id = (SELECT id
                                                        FROM airports
                                                        WHERE city = 'Fiftyville')
                    AND flights.year = 2021
                    AND flights.month = 7
                    AND flights.day = 29
                    ORDER BY flights.hour, flights.minute)
ORDER BY passengers.passport_number;


--interset and get the passport number from bank details and passengers

SELECT name,passport_number
FROM people
WHERE id IN (SELECT person_id
FROM bank_accounts
WHERE account_number IN (SELECT account_number
                            FROM atm_transactions
                            WHERE year = 2021
                            AND month = 7
                            AND day = 28
                            AND atm_location = 'Leggett Street'
                            AND transaction_type = 'withdraw'))

intersect
SELECT name, passengers.passport_number
FROM people
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON passengers.flight_id = flights.id
WHERE flights.year = 2021
AND flights.month = 7
AND flights.day = 29
AND flights.hour = 8
AND flights.minute = 20
AND flights.id IN (SELECT flights.id FROM airports
                    JOIN flights
                    ON airports.id = flights.destination_airport_id
                    WHERE flights.origin_airport_id = (SELECT id
                                                        FROM airports
                                                        WHERE city = 'Fiftyville')
                    AND flights.year = 2021
                    AND flights.month = 7
                    AND flights.day = 29
                    ORDER BY flights.hour, flights.minute)
ORDER BY passengers.passport_number;

-- Raymond said about phone call and get phonecaller and reciver.

SELECT name, phone_calls.duration
  FROM people
  JOIN phone_calls
    ON people.phone_number = phone_calls.caller
 WHERE phone_calls.year = 2021
   AND phone_calls.month = 7
   AND phone_calls.day = 28
   AND phone_calls.duration <= 60
UNION
SELECT name, phone_calls.duration
  FROM people
  JOIN phone_calls
    ON people.phone_number = phone_calls.receiver
 WHERE phone_calls.year = 2021
   AND phone_calls.month = 7
   AND phone_calls.day = 28
   AND phone_calls.duration <= 60
   ORDER BY phone_calls.duration;

-- Ruth - Car from Parking
SELECT name, bakery_security_logs.hour, bakery_security_logs.minute
  FROM people
  JOIN bakery_security_logs
    ON people.license_plate = bakery_security_logs.license_plate
 WHERE bakery_security_logs.year = 2021
   AND bakery_security_logs.month = 7
   AND bakery_security_logs.day = 28
   AND bakery_security_logs.activity = 'exit'
   AND bakery_security_logs.hour = 10
   AND bakery_security_logs.minute >= 15
   AND bakery_security_logs.minute <= 25
 ORDER BY bakery_security_logs.minute;


/*
from bank and flighter qry intersect , there are 4 ppl
+--------+-----------------+
|  name  | passport_number |
+--------+-----------------+
| Taylor | 1988161715      |
| Bruce  | 5773159633      |
| Luca   | 8496433585      |
| Kenny  | 9878712108      |
+--------+-----------------+
from lic plate
+---------+------+--------+
|  name   | hour | minute |
+---------+------+--------+
| Vanessa | 10   | 16     |
| Bruce   | 10   | 18     |
| Barry   | 10   | 18     |
| Luca    | 10   | 19     |
| Sofia   | 10   | 20     |
| Iman    | 10   | 21     |
| Diana   | 10   | 23     |
| Kelsey  | 10   | 23     |
+---------+------+--------+

*/
SELECT name
  FROM people
  JOIN bakery_security_logs
    ON people.license_plate = bakery_security_logs.license_plate
 WHERE bakery_security_logs.year = 2021
   AND bakery_security_logs.month = 7
   AND bakery_security_logs.day = 28
   AND bakery_security_logs.activity = 'exit'
   AND bakery_security_logs.hour = 10
   AND bakery_security_logs.minute >= 15
   AND bakery_security_logs.minute <= 25
INTERSECT
SELECT name
    FROM people
    WHERE id IN (SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (SELECT account_number
                            FROM atm_transactions
                            WHERE year = 2021
                            AND month = 7
                            AND day = 28
                            AND atm_location = 'Leggett Street'
                            AND transaction_type = 'withdraw'))

    INTERSECT
    SELECT name
    FROM people
    JOIN passengers
    ON people.passport_number = passengers.passport_number
    JOIN flights
    ON passengers.flight_id = flights.id
    WHERE flights.year = 2021
    AND flights.month = 7
    AND flights.day = 29
    AND flights.hour = 8
    AND flights.minute = 20
    AND flights.id IN (SELECT flights.id FROM airports
                    JOIN flights
                    ON airports.id = flights.destination_airport_id
                    WHERE flights.origin_airport_id = (SELECT id
                                                        FROM airports
                                                        WHERE city = 'Fiftyville')
                    AND flights.year = 2021
                    AND flights.month = 7
                    AND flights.day = 29
                    ORDER BY flights.hour, flights.minute)

;
/*
REDUCES SUSPECTS TO
+-------+
| name  |
+-------+
| Bruce |
| Luca  |
+-------+
But Luca is not in caller list, only recvied a call from Kathryn
*/
SELECT name, phone_calls.duration
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.receiver
WHERE phone_calls.year = 2021
AND phone_calls.month = 7
AND phone_calls.day = 28
AND phone_calls.duration <= 60
ORDER BY phone_calls.duration;

-- Hence Bruce alone appears to be in ATM, Caller, Passenger, Parking lot driver
-- Calls between Bruce and Robin based on duration of 45.

