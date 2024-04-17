import React, { useState, useEffect } from 'react'
import { Reveal } from '../Reveal'
import apiClient from '../../utils/ApiClient'
import axios from 'axios'


function Shop() {
  const [items, setItems] = useState([])
  const [nextPage, setNextPage] = useState(null)

  useEffect(() => {
    apiClient.get('inventory/item/list/')
      .then(response => {
        setItems(response.data.results)
        setNextPage(response.data.next)
      })
      .catch(error => {
        console.error('Error fetching data:', error)
      })
  }, [])

  const fetchNextPage = () => {
    if (nextPage) {
      axios.get(nextPage)
        .then(response => {
          setItems([...items, ...response.data.results])
          setNextPage(response.data.next)
        })
        .catch(error => {
          console.error('Error fetching next page:', error)
        })
    }
  }

    return (
      <>
        <div className="px-[50px] py-[100px]">
          <Reveal>
            <div className="flex justify-center text-[75px] font-medium"> <span className="text-[#00FF8A] pr-[20px]">SHOP</span> PAGE </div>
          </Reveal>
          <Reveal>
            <div className="flex justify-center">[ work in progress ]</div>
          </Reveal>

          <div className="flex justify-center w-full">
            <div className="grid grid-cols-3 gap-[25px]">
              {items.map(item => (
                <Reveal key={item.item_id}>
                  <div className="flex flex-col h-[400px] w-[300px] border border-gray-200 m-4 p-4">
                    <div className="ItemCard-Image" alt="Item Image">
                      <img src={item.item_profile_picture_link} alt={`${item.item_name} picture`} />
                    </div>
                    <p className="ItemCard-Name" alt="Item Name">{item.item_name}</p>
                    <p className="ItemCard-Brand" alt="Item Brand">{item.item_brand.item_brand_name}</p>
                    <p className="ItemCard-Price" alt="Item Price">Php {item.item_price}</p>
                  </div>
                </Reveal>
              ))}
            </div>
          </div>
            <Reveal>
              {nextPage && (
                <button onClick={fetchNextPage}>Load More</button>
              )}
            </Reveal>
        </div>
      </>
    )
  }

export default Shop