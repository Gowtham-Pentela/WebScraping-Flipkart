#!/usr/bin/env python
# coding: utf-8

# In[8]:


from autoscraper import AutoScraper
url="https://www.flipkart.com/search?q=ear+buds"
wanted_list=["Grostar TWS Twins Wireless Bluetooth Earphone with Mic...","₹249","75% off"]


# In[9]:


scraper=AutoScraper()
result=scraper.build(url,wanted_list)
print(result)


# In[10]:


scraper.get_result_similar(url,grouped=True)


# In[15]:


scraper.set_rule_aliases({'rule_7h6c':'Discount','rule_2u8r':'Price','rule_w6ut':'Title'})
scraper.keep_rules(['rule_7h6c','rule_2u8r','rule_w6ut'])
scraper.save('Ecommerce-Search')


# In[23]:


result=scraper.get_result_similar("https://www.flipkart.com/search?q=earphones",group_by_alias=True)


# In[24]:


result['Title']


# In[ ]:




