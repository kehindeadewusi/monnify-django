# monnify-django
Monnify Python App for easy integration of Monnify API.

```
Found some monnify implementation out there, they didn't have tests so I thought I'd have a whack at it in Spannish and Russian. Here's Spanish :)
```

## What is Monnify?
According to the usual yada-yada on Monnify website, Its is a payment gateway for businesses to accept payments from customers, either on a recurring or one-time basis. Monnify offers an easier, faster and cheaper way for businesses to get paid on their web and mobile applications using ...

```
https://www.monnify.com/
```

Monnify Provides some configurations that can be used on their sandbox, you should create yours really:

BaseUrl(Test): https://sandbox.monnify.com/
APIKEY: MK_TEST_SAF7HR5F3F
Contract Code: 4934121686
Secret Key: 4SY6TNL8CK3VPRSBTHTRG2N8XXEGC6NL

## API Categories
The monnify APIs are in various categories:

1. Disbursement : https://docs.teamapt.com/display/MON/Monnify+Disbursements
1. Collections: https://docs.teamapt.com/display/MON/Monnify+Collections
1. General Integration: Needed for disbursement and collections https://docs.teamapt.com/display/MON/General+Integration+Docs

```
The first implementation here focuses on Disbursement, this is my original use-case. Will probably visit collections shortly because it is my next use-case.
```
