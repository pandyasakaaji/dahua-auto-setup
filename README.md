# dahua-auto-setup

Automates Dahua device configuration via the RPC2 API (`POST /RPC2`).

- All requests are `POST` to `http://<device-ip>/RPC2` with a JSON body.
- Session token is obtained after login via `global.login`.

See [cgi.md](cgi.md) for full API reference.

---

## To-Do List

- [x] Find all APIs
- [x] Set all APIs
- [ ] Find API to use when the device is freshly initialized
- [ ] Automation script
