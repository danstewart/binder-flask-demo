# Binder Flask Demo

A small flask app to demonstrate the power of [binder](https://binder.danstewart.dev).  

### Get Started

```shell
pipenv run flask run --debug --port 1234
```

### TODO

- [ ] Rename `:mount-point` to target and allow targeting elements outside of frame
- [ ] If a `DynamicFrame` is set to not render on load but on load the state changes we should still reload
- [ ] If the URL changes on load then we see a flash of the default state
