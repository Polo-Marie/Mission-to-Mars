{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 90.0.4430\n",
      "Get LATEST driver version for 90.0.4430\n",
      "Driver [/Users/Irei/.wdm/drivers/chromedriver/mac64/90.0.4430.24/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "    mars = mongo.db.mars.find_one()\n",
    "    return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "    mars = mongo.db.mars\n",
    "    mars_data = scraping.scrape_all()\n",
    "    mars.update({}, mars_data, upsert=True)\n",
    "    return redirect('/', code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "ename": "OSError",
     "evalue": "[Errno 48] Address already in use",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-afe4f6debf34>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"__main__\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m     \u001b[0mapp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/flask/app.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self, host, port, debug, load_dotenv, **options)\u001b[0m\n\u001b[1;32m    988\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    989\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 990\u001b[0;31m             \u001b[0mrun_simple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhost\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mport\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    991\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    992\u001b[0m             \u001b[0;31m# reset the first request information if the development server\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/werkzeug/serving.py\u001b[0m in \u001b[0;36mrun_simple\u001b[0;34m(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, reloader_interval, reloader_type, threaded, processes, request_handler, static_files, passthrough_errors, ssl_context)\u001b[0m\n\u001b[1;32m   1050\u001b[0m         \u001b[0mrun_with_reloader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minner\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mextra_files\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreloader_interval\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreloader_type\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1051\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1052\u001b[0;31m         \u001b[0minner\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1053\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1054\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/werkzeug/serving.py\u001b[0m in \u001b[0;36minner\u001b[0;34m()\u001b[0m\n\u001b[1;32m    994\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mLookupError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    995\u001b[0m             \u001b[0mfd\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 996\u001b[0;31m         srv = make_server(\n\u001b[0m\u001b[1;32m    997\u001b[0m             \u001b[0mhostname\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    998\u001b[0m             \u001b[0mport\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/werkzeug/serving.py\u001b[0m in \u001b[0;36mmake_server\u001b[0;34m(host, port, app, threaded, processes, request_handler, passthrough_errors, ssl_context, fd)\u001b[0m\n\u001b[1;32m    845\u001b[0m         \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"cannot have a multithreaded and multi process server.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    846\u001b[0m     \u001b[0;32melif\u001b[0m \u001b[0mthreaded\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 847\u001b[0;31m         return ThreadedWSGIServer(\n\u001b[0m\u001b[1;32m    848\u001b[0m             \u001b[0mhost\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mport\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mapp\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrequest_handler\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpassthrough_errors\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mssl_context\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfd\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    849\u001b[0m         )\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/werkzeug/serving.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, host, port, app, handler, passthrough_errors, ssl_context, fd)\u001b[0m\n\u001b[1;32m    738\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0maddress_family\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0maf_unix\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexists\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mserver_address\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    739\u001b[0m             \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0munlink\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mserver_address\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 740\u001b[0;31m         \u001b[0mHTTPServer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mserver_address\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhandler\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    741\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    742\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mapp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mapp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/socketserver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, server_address, RequestHandlerClass, bind_and_activate)\u001b[0m\n\u001b[1;32m    450\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mbind_and_activate\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    451\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 452\u001b[0;31m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mserver_bind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    453\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mserver_activate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    454\u001b[0m             \u001b[0;32mexcept\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/http/server.py\u001b[0m in \u001b[0;36mserver_bind\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    136\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mserver_bind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    137\u001b[0m         \u001b[0;34m\"\"\"Override server_bind to store the server name.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 138\u001b[0;31m         \u001b[0msocketserver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTCPServer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mserver_bind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    139\u001b[0m         \u001b[0mhost\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mport\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mserver_address\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    140\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mserver_name\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetfqdn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhost\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/socketserver.py\u001b[0m in \u001b[0;36mserver_bind\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    464\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mallow_reuse_address\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    465\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msetsockopt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSOL_SOCKET\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSO_REUSEADDR\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 466\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mserver_address\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    467\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mserver_address\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetsockname\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    468\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mOSError\u001b[0m: [Errno 48] Address already in use"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
