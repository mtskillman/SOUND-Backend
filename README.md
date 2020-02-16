# SOUND Backend
Secret Key for testing: "OKP352FJMFDFBDG2", TOTP, SHA1 algorithm, 6 digits. Use resource-id of 2.<br/>
Contains two endpoints:
<br />
1. /sender-attempt:
    * Parameter **code**: 6 character string
    * Parameter **resource-id**: integer
    * Return: "access-token": "foo"
2. /receiver-attempt:
    * Parameter **token**: variable length string, JWT
    * Return: "result": "valid-token"

Error Codes:
<br />
* "missing-code-param" -> "code" parameter not found in request
* "missing-resource-id-param" -> "resource-id" parameter not found in request
* "invalid-resource-id" -> value of resource-id not valid option
* "failed-login" -> incorrect TOTP sent
* "missing-token-param" -> "token" parameter not found in request
* "token-not-issued-by-this-server" -> JWT is valid formatting, but not issued by this service
* "expired-token" -> JWT has expired
* "token-not-valid-formatting" -> string sent is not a JWT
* "unknown-error" -> other error occurred