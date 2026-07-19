import {useEffect,useState} from "react";


export function useNeuralTelemetry(){

    const [telemetry,setTelemetry] =
        useState<any>(null);


    useEffect(()=>{


        const timer =
            setInterval(()=>{


                setTelemetry({

                    temperature:
                        Math.floor(
                            45+
                            Math.random()*30
                        ),

                    workload:
                        Math.floor(
                            30+
                            Math.random()*60
                        ),

                    agents:
                        Math.floor(
                            5+
                            Math.random()*15
                        ),

                    health:
                        Math.floor(
                            90+
                            Math.random()*10
                        )

                });


            },2000);


        return ()=>clearInterval(timer);


    },[]);


    return telemetry;

}
