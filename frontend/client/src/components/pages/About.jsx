import React, { useEffect } from 'react'
import { Reveal } from '../Reveal'
import transition from '../Transition'

function About() {
  return (
    <>
      
      <div className="px-[50px] py-[100px]">
        <Reveal>
          <div className="flex justify-center text-[75px] font-medium"> <span className="text-[#00FF8A] pr-[20px]">ABOUT</span> PAGE </div>
        </Reveal>
        <Reveal>
          <div className="flex justify-center">[ work in progress ]</div>
        </Reveal>
      </div>
    </>
  )
}

export default transition(About);