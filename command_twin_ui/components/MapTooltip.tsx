export default function MapTooltip(
{
type,
id,
status,
temperature,
load
}
:any
){

return (

<div className="map-tooltip">

<h3>
{type}
:
{id}
</h3>


<p>
Status:
{status}
</p>


<p>
Temperature:
{temperature}°C
</p>


<p>
Load Health:
{load}%
</p>


</div>

)

}
