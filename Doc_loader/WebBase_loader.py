from langchain_community.document_loaders import WebBaseLoader

url = "https://www.amazon.in/ref=PS5BAU25QCPS5digital/dp/B0CY5QW186/?_encoding=UTF8&pd_rd_w=2Slrz&content-id=amzn1.sym.3b2d0011-a8ec-4315-a031-cca3c26cfcd6&pf_rd_p=3b2d0011-a8ec-4315-a031-cca3c26cfcd6&pf_rd_r=KJ4TM7XA1XKS3DPXX5WA&pd_rd_wg=k3X4e&pd_rd_r=d7ec20d7-d217-4a5d-938e-73ebf1545e26&ref_=pd_hp_d_atf_unk"

loader= WebBaseLoader(url)

docs=loader.load()

print(len(docs))
print(docs[0].page_content)