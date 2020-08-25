const express = require('express')
const app = express()
// app.use(require('cors')())
const server = require('http').Server(app)
const proxy = require('express-http-proxy')
const PORT = process.env.PORT || 3000
const { ExpressPeerServer } = require('peer')

// Redirect to https
function requireHTTPS (req, res, next) {
  // The 'x-forwarded-proto' check is for Heroku
  if (!req.secure && req.get('x-forwarded-proto') !== 'https' && process.env.NODE_ENV !== 'development') {
    return res.redirect('https://' + req.get('host') + req.url)
  }
  next()
}

app.use(requireHTTPS)
app.use('/peer', ExpressPeerServer(server))
app.use('/static/css', express.static('node_modules/antd/dist'))
app.use('/', proxy('http://localhost:8000', {
  proxyReqOptDecorator: (proxyReqOpts, srcReq) => {
    // Modify headers if running on Heroku
    proxyReqOpts.headers['X-Forwarded-Proto'] = PORT === 3000 ? 'http' : 'https'
    proxyReqOpts.headers.Host = PORT === 3000 ? 'localhost:3000' : 'rhappsody.herokuapp.com'
    return proxyReqOpts
  },
  limit: '100mb'
}))

server.listen(PORT)
console.log(`Peer server running on port ${PORT}`)
