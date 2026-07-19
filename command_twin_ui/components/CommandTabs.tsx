const tabs=[

"Overview",

"Fleet",

"Warehouse",

"Inventory",

"Risk",

"AI"

]


export default function CommandTabs(){

return (

<div className="command-tabs">

{
tabs.map(
tab=>

<button key={tab}>
{tab}
</button>

)
}

</div>

)

}
