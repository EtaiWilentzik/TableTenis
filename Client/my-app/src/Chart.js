import React, { useEffect, useRef } from 'react';
import './Chart.css';



const Chart = () => {
  const circle1Ref = useRef(null);


  useEffect(() => {
    const circle = circle1Ref.current;

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          // When the circle becomes visible
          circle.classList.add('visible');
          circle.classList.remove('hidden');
        } else {
          // When the circle becomes invisible
          circle.classList.add('hidden');
          circle.classList.remove('visible');
        }
      }
    );

    if (circle) {
      observer.observe(circle);
    }

    return () => {
      if (circle) {
        observer.unobserve(circle);
      }
    };
  }, []);


  return (
    <div>
      <svg width="158" height="158">
        <circle
          ref={circle1Ref}
          className="circle"
          cx="79"
          cy="79"
          r="44"
        />
      </svg>
    </div>
  );
};

export default Chart;